from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from crewai import Crew
from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks
from dotenv import load_dotenv
from flask_cors import CORS

from dotenv import load_dotenv

app = Flask(__name__)
CORS(app) 
socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")

class FinancialCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        financial_analyst_agent = agents.financial_analyst()
        investment_advisor_agent = agents.investment_advisor()

        research_task = tasks.research(research_analyst_agent, self.company)
        financial_task = tasks.financial_analysis(financial_analyst_agent)
        filings_task = tasks.filings_analysis(financial_analyst_agent)
        recommend_task = tasks.recommend(investment_advisor_agent)

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent,
            ],
            tasks=[research_task, financial_task, filings_task, recommend_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result
        
@app.route('/run_financial_analysis', methods=['POST'])
def run_financial_analysis():
    data = request.get_json()
    company = data.get('company')

    financial_crew = FinancialCrew(company)
    result = financial_crew.run()

    return jsonify({'result': result})

if __name__ == "__main__":
    socketio.run(app, debug=True)
