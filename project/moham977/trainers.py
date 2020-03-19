class personal_trainers :
    def __init__(self,name,discribtion,contact,price,qualifications,is_male_or_female,about_me):
        self.name = name
        self.discribtion = discribtion
        self.contact = contact
        self.price = price
        self.qualifications = qualifications
        self.is_male_or_female = is_male_or_female
        self.about_me = about_me
trainer1 = personal_trainers("jim","tall","000","£100","gcsc", "True", "nice")
trainer2 = personal_trainers("kaite","short","001","£90","gcse", "False","awesome")

