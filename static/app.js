const minTextAreaLength = 130;
const maxTextAreaLength = 1024;

const articleTextArea = document.getElementById('articleText');
const charCountElement = document.getElementById('charCount');

articleTextArea.addEventListener('input', updateCharCount);

function updateCharCount() {
    const articleText = articleTextArea.value.trim();

    charCountElement.textContent = `${articleText.length} / ${maxTextAreaLength}`;
    charCountElement.style.color = (articleText.length > maxTextAreaLength) ? '#FF3519' : '#000000'

}

async function summarizeText() {
    const summaryBlock = document.getElementsByClassName('summary__wrapper')[0];
    const summaryTextElement = document.getElementById('summaryText');
    const buttonElement = document.getElementById('summarizeButton');
    const summaryFormElement = document.getElementById('summaryForm');
    const errorTextElement = document.getElementById('errorText');

    const articleText = document.getElementById('articleText').value.trim();

    toggleErrorDisplaying(errorTextElement);

    if (articleText.length > minTextAreaLength && articleText.length <= maxTextAreaLength) {
        try {
            summaryFormElement.disabled = true;
            toggleButtonLoader(buttonElement, true);

            const summaryText = await getSummary(articleText);

            if (summaryText) {
                summaryTextElement.textContent = summaryText;
                summaryBlock.style.display = 'flex';
            } else {
                summaryBlock.style.display = 'none';
            }
        } catch (error) {
            toggleErrorDisplaying(errorTextElement, true, error);
        } finally {
            summaryFormElement.disabled = false;
            toggleButtonLoader(buttonElement, false);
        }
    } else if (articleText.length < minTextAreaLength) {
        toggleErrorDisplaying(errorTextElement, true, `The text field must have more than ${minTextAreaLength} characters.`);
    } else {
        toggleErrorDisplaying(errorTextElement, true, `The text field must have less than ${maxTextAreaLength} characters.`);
    }
}

function getSummary(articleText) {
    return fetch('/v1/get-summary', {
        method: 'POST',
        body: JSON.stringify({
            article: articleText
        }),
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Server error');
                });
            }

            return response.json();
        })
        .then(data => {
            return data.summary_text;
        })
        .catch(error => {
            console.error(error);
            throw error;
        });
}

function toggleButtonLoader(button, isLoading) {
    button.innerHTML = isLoading ? '<span class="loader"></span> Summarize' : 'Summarize';
    button.disabled = isLoading;
}

function toggleErrorDisplaying(textElement, isError = false, errorText = '') {
    textElement.textContent = isError ? errorText : '';
    textElement.style.display = isError ? 'block' : 'none';
}