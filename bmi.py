#Calculate bmi and report back to the user
# Uses functions to return the result.
# First function gather_info() collects weight, height and measurement system used.

def gather_info():
    weight = float(input("What is your weight (in pounds or kilograms) : "))
    height = float(input("What is your height (in inches or meters) : "))
    system = input("What system are you using for the units: Imperial or Metric: ").lower().strip()

    return(weight, height, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return Body Mass Index (BMI) for the given weigh, height, and measurement system
    :param weight:
    :param height:
    :param system:
    :return:
    """
    if system == 'metric':
        bmi = (weight / (height)**2)
    else:
        bmi = 703 * (weight / (height)**2)
    return bmi

while True:
    weight, height, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, height, system)
        print(f"Your BMI is {bmi}")
        break
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is {bmi}")
        break
    else:
        print("Error: Unknow System. Please input imperial or metric only")
