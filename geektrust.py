from sys import argv
import datetime
from src.subscription_details import subscription,topup

def process_input(lines):
    global date;amount=0
    is_music = False; is_podcast = False; is_video = False; is_subscription = False
    for line in lines:
        command = line.split(" ")
        #print(len(command))
        if len(command) == 2:
            date = command[1].strip('\n')
            # import pdb; pdb.set_trace()
            date = datetime.datetime.strptime(date, '%d-%m-%Y').date()

        # subscription logic
        if len(command) == 3:
            if command[0] == "ADD_SUBSCRIPTION":
                is_subscription = True
                category = command[1].strip('\n')
                type = command[2].strip('\n')
                if(category == "MUSIC"):
                    is_music = True
                
                if(category == "VIDEO"):
                    is_video = True

                if(category == "PODCAST"):
                    is_podcast = True
                
                create_subscription = subscription(date, category, type)
                amount+=create_subscription.amount()
                print("RENEWAL_REMINDER", category, create_subscription.amount(), create_subscription.renewal_date())

            # topup logic   
            if command[0] == "ADD_TOPUP":
                topup_type = command[1].strip('\n')
                topup_period = int(command[2].strip('\n'))
                add_topup = topup(topup_type, topup_period)
                #print(amount)
                amount+=add_topup.amount()
                print("TOPUP_AMOUNT", add_topup.amount())


    print("RENEWAL_AMOUNT", amount)
    return()

def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
     
    process_input(Lines)


    
                




    
if __name__ == "__main__":
    main()