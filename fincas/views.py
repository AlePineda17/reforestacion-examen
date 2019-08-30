from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse, get_object_or_404
from fincas.models import Property, Plot, Tree
from users.models import User


def index(request, user_id):
    template = 'fincas/index.html'
    context = {
        'index': Property.objects.all(),
        'user': get_object_or_404(User, id=user_id),
    }
    return render(request, template, context)


def create_property(request, user_id):
    if request.method == 'POST':
        new_property = Property(
            collaborator_id=request.POST['collaborator_id'],
            name=request.POST['name'],
            country=request.POST['country'],
            department=request.POST['department'],
        )
        new_property.save()
        return HttpResponseRedirect(reverse('fincas:index', kwargs={'user_id': user_id}))
    elif request.method == 'GET':
        template = 'fincas/create_property_form.html'
        context = {
            'user': User.objects.get(id=user_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def property_plots(request, user_id, property_id):
    template = 'fincas/property_plots.html'
    context = {
        'user': get_object_or_404(User, id=user_id),
        'plots': Plot.objects.filter(property=property_id),
        'property': get_object_or_404(Property, id=property_id),
    }
    return render(request, template, context)


def edit_property(request, property_id):
    if request.method == 'POST':
        updated_property = Property.objects.get(id=property_id)
        updated_property.name = request.POST['name']
        updated_property.country = request.POST['country']
        updated_property.department = request.POST['department']
        updated_property.save()
        return HttpResponseRedirect(reverse('fincas:index', kwargs={'user_id': updated_property.collaborator.id}))
    elif request.method == 'GET':
        template = 'fincas/edit_property_form.html'
        context = {
            'property': Property.objects.get(pk=property_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_property(request, property_id):
    deleted_property = Property.objects.get(id=property_id)
    deleted_property.delete()
    return HttpResponseRedirect(reverse('fincas:index', kwargs={'user_id': deleted_property.collaborator.id}))


def create_plot(request, user_id, property_id):
    if request.method == 'POST':
        new_plot = Plot(
            property_id=request.POST['property_id'],
            name=request.POST['name'],
            latitude=request.POST['latitude'],
            longitude=request.POST['longitude'],
        )
        new_plot.save()
        return HttpResponseRedirect(reverse('fincas:property_plots', kwargs={'user_id': user_id, 'property_id': new_plot.property.id}))
    elif request.method == 'GET':
        template = 'fincas/create_plot_form.html'
        context = {
            'user': User.objects.get(pk=user_id),
            'property': Property.objects.get(pk=property_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def plot_trees(request, user_id, plot_id, property_id):
    template = 'fincas/plot_trees.html'
    context = {
        'user': get_object_or_404(User, id=user_id),
        'trees': Tree.objects.filter(plot=plot_id),
        'plot': get_object_or_404(Plot, id=plot_id),
        'property': get_object_or_404(Property, id=property_id),
    }
    return render(request, template, context)


def edit_plot(request, user_id, plot_id):
    if request.method == 'POST':
        updated_plot = Plot.objects.get(id=plot_id)
        updated_plot.name = request.POST['name']
        updated_plot.latitude = request.POST['latitude']
        updated_plot.longitude = request.POST['longitude']
        updated_plot.save()
        return HttpResponseRedirect(reverse('fincas:property_plots', kwargs={'user_id': user_id, 'property_id': updated_plot.property.id}))
    elif request.method == 'GET':
        template = 'fincas/edit_plot_form.html'
        context = {
            'user': User.objects.get(pk=user_id),
            'plot': Plot.objects.get(id=plot_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_plot(request, plot_id, user_id):
    deleted_plot = Plot.objects.get(id=plot_id)
    deleted_plot.delete()
    return HttpResponseRedirect(reverse('fincas:property_plots', kwargs={'user_id': user_id, 'property_id': deleted_plot.property.id}))


def create_tree(request, user_id, property_id, plot_id):
    if request.method == 'POST':
        new_tree = Tree(
            plot_id=request.POST['plot_id'],
            diameter=request.POST['diameter'],
            height=request.POST['height'],
            health=request.POST['health'],
            year=request.POST['year'],
        )
        new_tree.save()
        return HttpResponseRedirect(reverse('fincas:plot_trees', kwargs={'user_id': user_id, 'property_id': property_id, 'plot_id': new_tree.plot.id}))
    elif request.method == 'GET':
        template = 'fincas/create_tree_form.html'
        context = {
            'user': User.objects.get(pk=user_id),
            'plot': Plot.objects.get(id=plot_id),
            'property': Property.objects.get(pk=property_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def edit_tree(request, user_id, property_id, tree_id):
    if request.method == 'POST':
        updated_tree = Tree.objects.get(id=tree_id)
        updated_tree.diameter = request.POST['diameter']
        updated_tree.height = request.POST['height']
        updated_tree.health = request.POST['health']
        updated_tree.year = request.POST['year']
        updated_tree.save()
        return HttpResponseRedirect(reverse('fincas:plot_trees', kwargs={'user_id': user_id, 'property_id': property_id, 'plot_id': updated_tree.plot.id}))
    elif request.method == 'GET':
        template = 'fincas/create_tree_form.html'
        context = {
            'user': User.objects.get(pk=user_id),
            'tree': Tree.objects.get(id=tree_id),
            'property': Property.objects.get(pk=property_id),
        }
        return render(request, template, context)
    return HttpResponse('Error: method not allowed.')


def delete_tree(request, user_id, property_id, tree_id):
    deleted_tree = Tree.objects.get(id=tree_id)
    deleted_tree.delete()
    return HttpResponseRedirect(reverse('fincas:plot_trees', kwargs={'user_id': user_id, 'property_id': property_id, 'plot_id': deleted_tree.plot.id}))
