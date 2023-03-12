# CI/CD - GITHUB ACTIONS WORKFLOW
GitHub actions are the built-in ci/cd tool for github.
CI/CD - continuous integration and continuous delivery
Essentially it allows us to automate the testing of our code to make sure it meets certain criteria after all the test are passed we can enable actions to automate the delivery of our code.
GitHub action workflow
We have workflow yaml file which specifies events, jobs, runners, steps and actions
Event = An event is a trigger for a workflow, a common event that occurs in a repository is when someone pushes new code, 
In the configuration file we can specify the workflow to trigger when someone pushes the new code, when the event occur its gonna run all the jobs within the workflow 
We can have multiple jobs within the event
And jobs which specifies multiple steps and actions(- name)
Runner - the runs on parameter - were we specify our runner = basically a container environment that will run our code by default github runs this container for us but we can host our own runner
Linter = its just something that we use to check to make sure that our code is conforming to certain standards. 
Super-linter is made up of multiple linters so it doesn’t matter which code we use in our repository 

DIrectory structure should be named correctly 
  .github/
      /workflow/
	Myworkflow.yml
When we commit this code and structure
The status icon will appear in our repo which will be initially yellow which means it’s currently running the workflow and checking the code, if all the checks pass then this icon will turn green check, if they fail then red cross.
To the see all the workflows you need to either click on that status icon or go onto the actions tab