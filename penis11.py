times= {"StopA":["06:55", "07:25", "07:55", "08:55", "09:55",
                "11:55", "14:00", "15:00", "15:30", "16:00"],
        "StopB":["06:40", "07:40", "08:40", "09:20", "09:40",
         "14:00", "15:00", "16:00", "16:30"]}

#a
print(times["StopB"][4])

#b
def time_value(time):
    return int(time[0:2] + time[3:5])

print(time_value(times["StopB"][4]))

#c
def next_bus(stop_name, current_time):
    for i in range(len(times[stop_name])):
        if time_value(times[stop_name][i]) > current_time:
            return times[stop_name][i]
    return "No more buses"
print(next_bus("StopB", 1013))
