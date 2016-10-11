#Event Planner

def _main_():
	#Variables
	events={}
	#Program
	response=raw_input("Open the event planner? (Y/N)")
	while response=="Y":
		decision=raw_input("Would you like to add(A) or remove(R) events, or check the agenda(C)?")
		if decision== "A":
			new_event=raw_input("Name of event: ")
			new_date=raw_input("Date of event: ")
			events[new_event]=new_date
		if decision== "R":
			event_removed==raw_input("Name of event to be removed: ")
			for event in events:
				if event_removed==event:
					remove_event(event, events)
				else:
					print "Event not found in planner."
		if decision=="C":
			for event in events:
				print event + events[event]

def remove_event(event, events):
	dict(new_events) = del events[event]
	return new_events

_main_()

		

