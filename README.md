# InterestMail- Email Generator for Job Applications

This project is an email generator designed to help you express your interest in job positions at various companies. 
By pasting the job posting link into the UI, it will scrape the content from the web page, analyze the job description, and generate a customized email. The email will include your skills and qualifications, crafted using **Llama-3.12-70B** (Groq Cloud).

## Features

- **Job Posting Scraping:** Paste the job posting URL into the UI, and the tool will scrape the relevant content from the webpage.
- **Email Generation:** It generates an email that includes your skills and expresses your interest in the position, personalized based on the job posting.
- **Groq Cloud API Integration:** Uses **Llama-3.12-70B** (Groq Cloud) for natural language processing to generate the email content.

## Setup and Installation

To run this project locally, follow the steps below:

### 1. Install Dependencies

First, make sure you have the necessary Python dependencies installed. You can do this by running the `requirements.txt` file. 
This will install all the required libraries for the project.

### 2. API Key

In order to use Groq Cloud's Llama-3.12-70B model, you will need an API key. 
You can create your own API key by registering on [Groq Cloud](https://groq.com/). Once you have your API key, replace the existing placeholder with your API key in the configuration file or wherever the API key is required in the project.

### 3. Replace Portfolio CSV with Your CSV File

This project includes a `portfolio.csv` file that contains project links. 
You need to replace it with a CSV file that contains links to your own projects. Make sure the format follows the required structure for easy integration with the email generation.

### 4. Run the Application

Once the dependencies are installed and the necessary files are replaced, you can run the application locally. Follow the instructions provided in the UI to scrape job postings and generate emails.


## Notes

- Make sure to replace the placeholder API key with your own Groq Cloud API key to access the Llama-3.12-70B model.
- The CSV file should contain your project links in a format that the generator can process.
- The tool scrapes job postings and creates a personalized email using the scraped content and your skills. Ensure the job posting link you provide is publicly accessible.

## License

This project is open-source, and you are free to modify it for your own use. Make sure to credit the original authors if you decide to distribute the code.

---

Feel free to reach out if you have any questions or run into issues with setup or usage.


