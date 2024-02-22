import os
import pandas as pd
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from datetime import date

# Load environment variables
load_dotenv()

app = FastAPI()


class TradingInput(BaseModel):
    indicator: str
    time_period: str
    symbol: Optional[str] = None
    frequency: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    risk_tolerance: Optional[float] = None
    profit_target: Optional[float] = None


# Initialize OpenAI instances
llm = AzureChatOpenAI(
    openai_api_version="API Version",
    azure_deployment="Deployement Name",
    azure_endpoint="End Point",
    api_key="API Key",
)


# Define trading strategy
def get_trading_strategy(
    indicator: str,
    time_period: str,
    symbol: Optional[str] = None,
    frequency: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    risk_tolerance: Optional[float] = None,
    profit_target: Optional[float] = None,
) -> str:
    research_template = """look at the recent market data for NASDAQ and make a trading strategy for it. use {indicator} of your choice. over the last {time_period} days.
       Don't say As an artificial intelligence, I don't have real-time access to market data or the ability to create real-time trading strategies.
    """
    research_prompt = PromptTemplate(
        template=research_template, input_variables=["indicator", "time_period"]
    )
    research_chain = LLMChain(prompt=research_prompt, llm=llm)
    research_result = research_chain.run(
        {"indicator": indicator, "time_period": time_period}
    )
    return research_result


def get_trading_instructions(
    trading_strategy: str,
    symbol: Optional[str] = None,
    frequency: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    risk_tolerance: Optional[float] = None,
    profit_target: Optional[float] = None,
) -> str:
    instructions_template = """  
    Based on the generated trading strategy:  
    - Determine the entry condition.  
    - Define the exit condition.  
    - Specify the market stay-out condition.  
  
    Trading Strategy:  
    {trading_strategy}  
    Entry Instructions:  
    ...  
    Exit Instructions:  
    ...  
    Market Stay-out Instructions:  
    ...   
    """
    instruction_prompt = PromptTemplate(
        template=instructions_template, input_variables=["trading_strategy"]
    )
    instruction_chain = LLMChain(prompt=instruction_prompt, llm=llm)
    instruction_result = instruction_chain.run({"trading_strategy": trading_strategy})
    return instruction_result


# Generate backtest code
def get_backtest_code(
    trading_strategy: str,
    trading_instructions: str,
    symbol: Optional[str] = None,
    frequency: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    risk_tolerance: Optional[float] = None,
    profit_target: Optional[float] = None,
) -> str:
    backtesting_template = """  
    Please code a backtest for this trading strategy with backtesting.py then output the full backtest code. This is the {trading_strategy} and instruction you should follow {trading_instructions} 
    
    Example Strategy:

    import pandas as pd  
    from backtesting import Backtest, Strategy  
    from backtesting.lib import crossover  
    from backtesting.test import GOOG  
  
    # Define the trading strategy  
    class MyStrategy(Strategy):  
        def init(self):  
            close = self.data.Close  
            self.ma1 = self.I(pd.Series.rolling, close, 10)  
            self.ma2 = self.I(pd.Series.rolling, close, 50)  
  
        def next(self):  
            if crossover(self.ma1, self.ma2):  
                self.buy()  
            elif crossover(self.ma2, self.ma1):  
                self.sell()  
  
    # Create a backtesting instance  
    bt = Backtest(GOOG, MyStrategy, cash=10000, commission=.002)  
  
    # Run the backtest  
    stats = bt.run()  
  
    # Print the results  
    print(stats)  
    """
    backtesting_prompt = PromptTemplate(
        template=backtesting_template,
        input_variables=["trading_strategy", "trading_instructions"],
    )
    backtesting_chain = LLMChain(prompt=backtesting_prompt, llm=llm)
    backtesting_result = backtesting_chain.run(
        {
            "trading_strategy": trading_strategy,
            "trading_instructions": trading_instructions,
        }
    )
    return backtesting_result


@app.post("/generate_strategy/")
async def generate_and_backtest_strategy(trading_input: TradingInput):
    strategy = get_trading_strategy(
        trading_input.indicator,
        trading_input.time_period,
        trading_input.symbol,
        trading_input.frequency,
        trading_input.start_date,
        trading_input.end_date,
        trading_input.risk_tolerance,
        trading_input.profit_target,
    )
    instructions = get_trading_instructions(
        strategy,
        trading_input.symbol,
        trading_input.frequency,
        trading_input.start_date,
        trading_input.end_date,
        trading_input.risk_tolerance,
        trading_input.profit_target,
    )
    backtest_code = get_backtest_code(
        strategy,
        instructions,
        trading_input.symbol,
        trading_input.frequency,
        trading_input.start_date,
        trading_input.end_date,
        trading_input.risk_tolerance,
        trading_input.profit_target,
    )
    return {
        "strategy": strategy,
        "instructions": instructions,
        "backtest_code": backtest_code,
    }
