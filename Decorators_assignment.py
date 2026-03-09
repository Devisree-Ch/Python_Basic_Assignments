# 1] Create a decorator called welcome_message that prints "Welcome!" before running a function.
# Apply it to a function called start_program() that prints "Program started".
print("------------------------Scenario 1-----------------------------")
def welcome_message(func):
	def inner():
		print("Welcome!")
		func()
	return inner

@welcome_message
def start_program():
	print("Program started")
start_program()

# 2] Create a decorator called after_message that prints "Task completed" after the function runs.
# Apply it to a function called run_task() that prints "Task is running".
print("------------------------Scenario 2-----------------------------")
def after_message(func):
	def inner():
		func()
		print("Task completed")
	return inner

@after_message
def run_task():
	print("Task is running")
run_task()

# 3] Create a decorator called repeat_two_times that runs a function two times whenever it is called.
# Apply it to a function called practice() that prints "Keep practicing Python".
print("------------------------Scenario 3-----------------------------")
def repeat_two_times(func):
	def inner():
		func()
		print("first time")
		func()
		print("second time")
	return inner

@repeat_two_times
def practice():
	print("Keep practicing python")
practice()

# 4] Create a decorator called simple_log that prints "Function is executing..." before running the function.
# Apply it to a function called calculate() that prints "Calculation done".
print("------------------------Scenario 4-----------------------------")
def simple_log(func):
	def inner():
		print("Function is executing...")
		func()
	return inner

@simple_log
def calculate():
	print("Calculation done")
calculate()

# 5] Create a decorator called start_end that prints "Start" before the function and "End" after the function runs.
# Apply it to a function called process() that prints "Processing data"
print("------------------------Scenario 5-----------------------------")
def start_end(func):
	def inner():
		print("Start")
		func()
		print("End")
	return inner

@start_end
def process():
	print("Processing data")
process()