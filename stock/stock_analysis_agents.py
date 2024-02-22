from crewai import Agent
import os
from dotenv import load_dotenv
from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools
from langchain_openai import AzureChatOpenAI
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

load_dotenv()

default_llm = AzureChatOpenAI(
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
    api_key=os.environ.get("AZURE_OPENAI_KEY"),
)


class StockAnalysisAgents:
    def financial_analyst(self):
        return Agent(
            role="The Best Financial Analyst",
            llm=default_llm,
            goal="""Impress all customers with your financial data 
      and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k,
            ],
        )

    def research_analyst(self):
        return Agent(
            role="Staff Research Analyst",
            goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
            llm=default_llm,
            backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool(),
                SECTools.search_10q,
                SECTools.search_10k,
            ],
        )

    def investment_advisor(self):
        return Agent(
            role="Private Investment Advisor",
            goal="""Impress your customers with full analyses over stocks
      and completer investment recommendations""",
            llm=default_llm,
            backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
            verbose=True,
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool(),
            ],
        )
