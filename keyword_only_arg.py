def convert_to_cm_from_meter(*, meter):
    return meter * 100

print(convert_to_cm_from_meter(10))     #error: keyword only arg error
print(convert_to_cm_from_meter(meter=10))

