from django.shortcuts import render
from django.http import *
from .models import TodoItem
from django.contrib import messages


def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request,'todo.html',
		{'all_items': all_todo_items})

def addTodo(request):
	new_item = TodoItem(content = request.POST['content']) #create a new todo all_items
	new_item.save() # save
	return HttpResponseRedirect('/todo/') #redirect the browser to '/todo/'

def deleteTodo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/todo/')

# def updateTodo(request, todo_id):
# 	item_to_update = TodoItem.objects.get(id=todo_id)
# 	item_to_update.update()
# 	return HttpResponseRedirect('/todo/')

# def updateTodo(request, todo_id):
#     if request.method == 'POST':
#         item_to_update = TodoItem.objects.get(id=todo_id)

#         form = TodoItem(request.POST, instance=todo)

#         if form.is_valid():
#             form.save()
#             messages.success(request, ('Item has been edited.'))
#             return HttpResponseRedirect('/todo/')

#     else:
#         item_to_update = TodoItem.objects.get(id=todo_id)
#         return render(request, 'todo.html', {'all_items': all_todo_items})
