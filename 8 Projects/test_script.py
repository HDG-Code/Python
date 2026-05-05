# this:- "968-Maria, ( Data Engineer ) ;; 27y " to this :- name: maria | role: data engineer | age: 27
                
a = "968-Maria, ( Data Engineer ) ;; 27y "

print(a.replace("968-", "Name: ").replace(", (", " | Role: ").replace(" ) ;; ", " | Age: ").replace("y", ""))