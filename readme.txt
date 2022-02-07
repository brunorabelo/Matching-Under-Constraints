Structure of files:
_ algorithms
|______ task2.py
|______ task3.py
|______ task5.py
|______ task7.py
_ instances
|______ instance1.py
|______ instance2.py
|______ instance3.py
_utils.py
_main.py
_task6.py
_task8.py
_task9.py
_Tasks.ipynb
_task6.py
_requirements.txt

To use these codes is necessary to install the dependencies in requirements.txt it is also sugested to create a python's virtual enviroment.

To install the dependencies: 
    pip install -r requirements.txt

Once the dependencies are installed, it is possible to use the scripts.

The "main.py" shows one possible way to execute on instance of with an implemented algorithm.

Basically, to execute an algorithm we need an matching_table (preferences table), a schools list, and a students list.

Each instance file (ex. "instance1.py") has a method "generate_matching_table_schools_and_students" that creates the parameters we need to execute an algorithm.
The instances instance2 and instance3 require a "n" parameter in the method "generate_matching_table_schools_and_students".

Having created theses parameters, we can execute the algorithm we want.

To execute an algorithm we create a new object of it. For example, the algorithm "DeferredAcceptanceAlgoCapacityConstraint" located in the file "task3.py":
    algo = DeferredAcceptanceAlgoCapacityConstraint(matching_table, schools, students)
    results = algo.execute()

Then we have the results.

For the algorithm "FixedPointAlgorithm" located in the file "task7.py" we also need a constraint function in order to create an object. Ex:

    result_task2_instance1 = task7.FixedPointAlgorithm(matching_table, schools, students, task8_constraints).execute()

where task8_constraints is whatever function that takes two paremeters (school, demand) and return true or false:
 For example:
    def task8_constraints(school, demand):
        return len(demand) <= school.capacity

With all of that, we are able to execute all the tasks proposed in the Projet.

We tried to design the architecture of the project as intuitive as possible.

It is also possible, to execute the jupyter notebook in "Tasks.ipynb" and have some graphics plotted on.

emails: 
bruno.rabelo-wenchenck-botelho@polytechnique.edu
mauricio.de-moura-lima@polytechnique.edu