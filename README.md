# 📧 Cold Mail Generator

A cold outreach system for service companies built using Groq, Langchain, and Streamlit. Users can input the URL of a company's careers page, and the tool extracts job listings from the page, then generates personalized cold emails. These emails include relevant portfolio links, sourced from a vector database, tailored to the specific job descriptions.

### **Project Overview & Strengths**:
- The app automates cold email generation by scraping job descriptions and customizing outreach based on relevant portfolio projects.
- It integrates cutting-edge NLP techniques (ChatGroq and Langchain) to streamline job scraping and email writing.
- The use of ChromaDB for querying portfolio information adds a strong personalized touch by matching the company’s tech stack with job requirements.

## Architecture Diagram
![image](https://github.com/user-attachments/assets/81a926f9-6953-4098-b380-831398087ef2)


## Set-up
1. To get started we first need to get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 


2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```

### **Areas to Enhance**:
1. **Error Handling**: The main script handles errors at the top level, but more granular error handling (e.g., for scraping failures or database issues) could help improve user experience.
2. **Documentation**: Adding comments to clarify the purpose of each method (especially in `chains.py`) would make the code more maintainable.
3. **Flexibility for Different Job Sites**: The URL scraping is currently hardcoded for one format; adding more flexible parsing techniques could expand its usability to other job platforms.
4. **Environment Variables**: The API key for ChatGroq is loaded from an environment variable (`GROQ_api_KEY`). Ensure this is securely managed in deployment.

## Future Aspects
The future of this system using Groq, Langchain, and Streamlit is bright, with the potential to revolutionize outreach through automation and AI-driven personalization. As these technologies advance, the tool can generate highly targeted emails. Enhanced integration with various outreach plateform, to build a complete automated outreach system. 
This level of personalization at scale will streamline the job application process, increasing the chances of engagement and making it a valuable tool for service companies or individuals.

