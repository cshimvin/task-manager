from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # unique=True ensures it's a unique value and nullable=False ensures it is not empty
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # This references the Task class and targets the category id. Therefore, if the category
    # is deleted then the tasks will be deleted as well. Needs the statement commented in the
    # Task class below 
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name

class Task(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # ondelete="CASCADE" means if the category id is deleted
    # then the tasks will also be delted to prevent an error 
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete="CASCADE"), nullable=False)
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
