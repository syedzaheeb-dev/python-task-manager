import json
import os

file_name = 'practice.json'

class Task:
    def __init__(self, id , task, status):
        
        self.id = id
        self.task = task
        self.status = status

    def get_dict(self):
        return {
            "ID" : self.id,
            "task"  : self.task,
            "status" : self.status
        }   
    
class Management():
    def __init__(self):
        self.data = self._load_data()
    
    def _load_data(self):
        if not os.path.exists(file_name):
            return []

        try:
            with open(file_name , "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
        
    def _save_data(self):
        with open(file_name , "w") as f:
            return json.dump(self.data ,f ,indent=4)
    
    def add_task(self ,id,task ,status):
        for d in self.data:

            if d['ID'] == id:
                print("---You Can't write two different tasks on same Id---")
                return
            
            elif not id.startswith("T"): 
                print('---Id Type Does not Meet the requirements---')
                return
            

        data = Task(id ,task , status)
        self.data.append(data.get_dict())
        self._save_data()
        print("\n---Task Added Successfully---\n")
                    

    def complete_task(self ,id):

        found = False
        for data in self.data:
            if data['ID'] == id:
                found = True
                if data['status'] == False:
                    data['status'] = True
                    print(f"{'-' * 35}\n{data['task']}\nCompleted Successfully.\n{'-' * 35}")
                    break
                else:
                    print("---You Already Completed the task---")
                    break
        if not found:
            print(f"---Task On this ID : {id} , Does Not Found---")
        self._save_data()
                
    def remove_task(self, id):
        removed_task_id = False
        found = False

        for data in self.data:
            if data['ID'] == id:
                found = True
                if data['status'] == False:
                    print(f"{'-' * 35}\nStatus : {data['status']} | Not Completed yet.\n"
                          f"Nice TRY Buddy But you Can't Remove before Completing It😎😎.\n{'-' * 35}")
                    return
                else:
                    removed_task_id = True
                    print(f"{'-'*35}\nTask {data['ID']} Removed Successfully.\n{'-'*35}")
                    self.data.remove(data)
        if not found:
            print(f"---Task On this ID : {id} , Does Not Found---")
            return                
            
        if removed_task_id:
            previous_task_id = int(id[1:])
            for data in self.data:
                current_task_id = int(data['ID'][1:])

                if current_task_id > previous_task_id:
                    new_task_id = current_task_id - 1

                    data['ID'] = f"T{new_task_id:03d}"
                    
        self._save_data()

    def view_task(self):
        if not self.data:
            print("---There is No Data to look for---\n")
            return

        for index , data in enumerate(self.data, start=1):
            print('-' * 35)
            print(f"{index}. {data}\n")

manager = Management()    
def menu():
    actions = ['Add Task' , 'Complete Task', 'Remove Tasks' ,'View Tasks' , 'Exit' ]
    while True:
        for i , d in enumerate(actions , start=1):
            print(f"{i}. {d}")
        choice = input("Choose : ").strip()
        print("-"*35)
        if choice == "1":

            id = input("Enter the id: ").strip()
            task = input("Enter the Task:\n\t|").strip()
            status = False
        
            manager.add_task(id,task,status)
        
        elif choice == "2":
            id = input("Enter the id: ").strip()
            manager.complete_task(id)

        elif choice == "3":
            id = input("Enter id to Remove Task: ").strip()

            manager.remove_task(id)

        elif choice == "4":
            manager.view_task()

        elif choice == "5":
            print("---Exitting the System---")
            break
        else:
            print("---Invalid Choice---")
        

if __name__ == "__main__":
    menu()
