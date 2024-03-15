# ProposalTutor

ProposalTutor is a Streamlit application designed to assist researchers in refining their proposals by providing comprehensive feedback on clarity, feasibility, novelty, methods, and cases. The application allows users to upload their research proposals in DocX format and receive specific feedback based on the content of their proposal and additional criteria they may wish to include.

## Features

- **Proposal Upload**: Users can upload their research proposal documents for analysis.
- **Customizable Feedback**: Feedback is generated on various aspects of the proposal, including clarity, feasibility, novelty, methods, and specific user-defined criteria.
- **Support for Multiple Criteria**: Users can specify additional criteria for more tailored feedback.
- **Streamlit Interface**: A simple and interactive UI for easy navigation and usage.

## Getting Started

### Prerequisites

Before running ProposalTutor, ensure you have the following installed:
- Python 3.6 or higher
- Streamlit
- Required Python packages (`docx2txt`, `openai`, etc.)

### Installation

1. Clone the repository to your local machine:
```sh
git clone https://github.com/JonasWeinert/ProposalFeedback.git
```

2. Navigate to the cloned repository:
```sh
cd ProposalFeedback
```

3. Install the required Python packages:
```sh
pip install -r requirements.txt
```

### Running the Application

To run the application, execute the following command in your terminal:
```sh
streamlit run app.py
```

## How to Use

1. **Start the Application**: Open your browser and go to the local URL provided by Streamlit, typically `http://localhost:8501`.

2. **Upload Your Proposal**: In the "Upload your Proposal" section, choose your DocX file containing the research proposal.

3. **Specify Additional Criteria**: If applicable, add additional criteria in the sidebar for more specific feedback.

4. **Generate Feedback**: Click the "Submit!" button to receive feedback on your proposal.

## Customizing the App

You can customize the language model used for generating feedback by editing the `llm` variable in `app.py` and `util.py` files. Supported models include variants of GPT-3.5 and GPT-4.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. If you find any bugs or have suggestions, please open an issue in the GitHub repository.

## Acknowledgements

- Streamlit for the interactive web application framework.
- OpenAI for the GPT language models used for generating feedback.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

--- 

