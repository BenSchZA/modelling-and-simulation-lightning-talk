setup:
	python3.10 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt

run_agent_based_model:
	. venv/bin/activate; python agent_based_model.py

run_system_dynamics_model:
	. venv/bin/activate; python system_dynamics_model.py
