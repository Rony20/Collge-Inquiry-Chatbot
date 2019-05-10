from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import aiml
import os
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
total_response = []
total_response_2 = []
 
class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])
	 
	@app.route("/", methods=['GET', 'POST'])
	def hello():
		is_url = False
		kernel_response = ''
		form = ReusableForm(request.form)
		 
		#print(form.errors)
		if request.method == 'POST':
			name=request.form['name']
			print(name)
		 
		if form.validate():
		# Save the comment here.

			#print(os.getcwd())
			# Create the kernel and learn AIML files
			kernel = aiml.Kernel()
			kernel.learn("std-startup.xml")
			kernel.respond("load aiml b")

			# Press CTRL-C to break this loop
			#while True:
			#print(kernel.respond(input("Enter your message >> ")))
			#ans_form_dataset = kernel.respond(input("Enter your message >> "))

			user_message = request.form['name']
			sem = {'sem-1':'sem1', 'sem-2':'sem2', 'sem-3':'sem3', 'sem-4':'sem4', 'sem-5':'sem5', 'sem-6':'sem6', 'sem-7':'sem7', 'sem-8':'sem8'}
			department = ['Computer', 'IT', 'Electronics', 'Electrical', 'Mechanical', 'Civil', 'Production', 'EC']

			user_message_list = user_message.split(" ")
			#print(user_message_list)

			dept_response = ''
			sem_response = ''
			for msg in user_message_list:
				if msg in department:
					dept_response = msg
				if msg in sem:
					sem_response = sem[msg]

			print(dept_response)
			print(sem_response)
			

			if dept_response == '' or sem_response == '':
				kernel_response = kernel.respond(user_message)
				if kernel_response == '':
					kernel_response = 'Give me a proper question'
				total_response.append('Bot  : ' + kernel_response)
				total_response.append('User : ' + user_message)
				flash('User : ' + user_message)
				flash('Bot  : ' + kernel_response)
			else:
				print(dept_response)
				print(sem_response)
				find_response = dept_response + " " + sem_response
				print('Nothing')
				kernel_response = kernel.respond(find_response)
				print(kernel_response)
				
				total_response.append('Bot  : ' + kernel_response)
				total_response.append('User : ' + user_message)

				if '//' in kernel_response:
					is_url = True

				#print(find_response)
				flash('User : ' + user_message)
				flash('Bot  : ' + kernel_response)

		else:
			flash('All the form fields are required. ')
		
		print(total_response)
		total_response_2 = total_response
		print(total_response_2)
		total_response_2 = total_response_2[::-1]
		print(total_response_2)
		context = {
				'form':form,
				'is_url':is_url,
				'kernel_response':kernel_response,
				'total_response':total_response_2
			}
		 
		return render_template('hello.html', context=context)
 
if __name__ == "__main__":
	app.run()
