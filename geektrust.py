from sys import argv
import datetime
from src.subscription_details import subscription,topup
from src.errors import SUBSCRIPTIONS_NOT_FOUND_ERROR, ADD_SUBSCRIPTION_FAILED_ERROR, ADD_TOPUP_FAILED_ERROR, INVALID_DATE_ERROR
def process_input(lines):
    global date;subscriptions=[];amount=0
    is_music = False; is_podcast = False; is_video = False; is_subscription = False; is_topup = False; is_error = False
    for line in lines:
        command = line.split(" ")

        #if command is START_SUBSCRIPTION
        if len(command) == 2:
            date = command[1].strip('\n')
            try:
                date = datetime.datetime.strptime(date, '%d-%m-%Y').date()
            except ValueError:
                is_error = True
                print(INVALID_DATE_ERROR["INVALID_DATE"])

        # subscription logic
        if len(command) == 3:
            if command[0] == "ADD_SUBSCRIPTION":
                is_subscription = True
                category = command[1].strip('\n')
                type = command[2].strip('\n')

                #checking if music subscription is added twice
                if(category == "MUSIC"):
                    if is_music == True:
                        is_error = True
                        print(ADD_SUBSCRIPTION_FAILED_ERROR["ADD_SUBSCRIPTION_FAILED_ERROR"], ADD_SUBSCRIPTION_FAILED_ERROR["DUPLICATE_CATEGORY"])
                    is_music = True
                
                #checking if video subscription is added twice
                if(category == "VIDEO"):
                    if is_video == True:
                        is_error = True
                        print(ADD_SUBSCRIPTION_FAILED_ERROR["ADD_SUBSCRIPTION_FAILED_ERROR"], ADD_SUBSCRIPTION_FAILED_ERROR["DUPLICATE_CATEGORY"])
                    is_video = True

                #checking if podcast subscription is added twice
                if(category == "PODCAST"):
                    if is_podcast == True:
                        is_error = True
                        print(ADD_SUBSCRIPTION_FAILED_ERROR["ADD_SUBSCRIPTION_FAILED_ERROR"], ADD_SUBSCRIPTION_FAILED_ERROR["DUPLICATE_CATEGORY"])
                    is_podcast = True
                
                create_subscription = subscription(date, category, type)
                amount+=create_subscription.amount()
                subscriptions.append(create_subscription)
    
            # topup logic   
            if command[0] == "ADD_TOPUP":

                #checking is subscription is added or not
                if not is_subscription:
                    is_error = True
                    print(ADD_TOPUP_FAILED_ERROR["ADD_TOPUP_FAILED"], SUBSCRIPTIONS_NOT_FOUND_ERROR["SUBSCRIPTIONS_NOT_FOUND"])
                    continue
                
                #checking if topup is added twice
                if is_topup:
                    is_error = True
                    print(ADD_TOPUP_FAILED_ERROR["ADD_TOPUP_FAILED"], ADD_TOPUP_FAILED_ERROR["DUPLICATE_TOPUP"])
                    continue
                
                is_topup = True
                topup_type = command[1].strip('\n')
                topup_period = int(command[2].strip('\n'))
                add_topup = topup(topup_type, topup_period)
                #print(amount)
                amount+=add_topup.amount()
                #print("TOPUP_AMOUNT", add_topup.amount())

        if len(command) == 1:
            if not is_subscription:
                is_error = True
                print(SUBSCRIPTIONS_NOT_FOUND_ERROR["SUBSCRIPTIONS_NOT_FOUND"])
                continue
            if not is_error:
                for subs in subscriptions:
                    print("RENEWAL_REMINDER", subs.category, subs.renewal_date())
                print(amount)

    

def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
     
    process_input(Lines)


    
                




    
if __name__ == "__main__":
    main()