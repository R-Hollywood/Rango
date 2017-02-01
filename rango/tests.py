from django.test import TestCase


from django.core.urlresolvers import reverse

from django.contrib.staticfiles import finders

from rango.forms import CategoryForm, PageForm

# Thanks to Enzo Roiz https://github.com/enzoroiz who made these tests during an internship with us



class GeneralTests(TestCase):

    def test_serving_static_files(self):

        # If using static media properly result is not NONE once it finds rango.jpg

        result = finders.find('images/rango.jpg')

        self.assertIsNotNone(result)





class IndexPageTests(TestCase):

        

    def test_index_contains_hello_message(self):

        # Check if there is the message 'Rango Says'

        # Chapter 4

        response = self.client.get(reverse('index'))

        self.assertIn(b'Rango says', response.content)

         

    def test_index_using_template(self):

        # Check the template used to render index page

        # Chapter 4

        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'rango/index.html')



    def test_rango_picture_displayed(self):

        # Check if is there an image called 'rango.jpg' on the index page

        # Chapter 4

        response = self.client.get(reverse('index'))

        self.assertIn(b'img src="/static/images/rango.jpg', response.content)

    

    def test_index_has_title(self):

        # Check to make sure that the title tag has been used

        # And that the template contains the HTML from Chapter 4 

        response = self.client.get(reverse('index'))

        self.assertIn(b'<title>', response.content)

        self.assertIn(b'</title>', response.content)





class AboutPageTests(TestCase):

        

    def test_about_contains_create_message(self):

        # Check if in the about page is there - and contains the specified message

        # Exercise from Chapter 4

        response = self.client.get(reverse('about'))

        self.assertIn(b'This tutorial has been put together by', response.content)

        

        

    def test_about_contain_image(self):

        # Check if is there an image on the about page

        # Chapter 4

        response = self.client.get(reverse('about'))

        self.assertIn(b'img src="/static/images/', response.content)

        

    def test_about_using_template(self):

        # Check the template used to render index page

        # Exercise from Chapter 4 

        response = self.client.get(reverse('about'))



        self.assertTemplateUsed(response, 'rango/about.html')

        

        

        

class ModelTests(TestCase):



    def setUp(self):

        try:

            from populate_rango import populate

            populate()

        except ImportError:

            print('The module populate_rango does not exist')

        except NameError:

            print('The function populate() does not exist or is not correct')

        except:

            print('Something went wrong in the populate() function :-(')

        

        

    def get_category(self, name):

        

        from rango.models import Category

        try:                  

            cat = Category.objects.get(name=name)

        except Category.DoesNotExist:    

            cat = None

        return cat

        

    def test_python_cat_added(self):

        cat = self.get_category('Python')  

        self.assertIsNotNone(cat)

         

    def test_python_cat_with_views(self):

        cat = self.get_category('Python')

        self.assertEquals(cat.views, 128)

        

    def test_python_cat_with_likes(self):

        cat = self.get_category('Python')

        self.assertEquals(cat.likes, 64)

        



class Chapter4ViewTests(TestCase):

    def test_index_contains_hello_message(self):

        # Check if there is the message 'hello world!'

        response = self.client.get(reverse('index'))

        self.assertIn('Rango says', response.content)



    def test_does_index_contain_img(self):

        # Check if the index page contains an img

        response = self.client.get(reverse('index'))

        self.assertIn('img', response.content)



    def test_about_using_template(self):

        # Check the template used to render index page

        # Exercise from Chapter 4

        response = self.client.get(reverse('about'))



        self.assertTemplateUsed(response, 'rango/about.html')



    def test_does_about_contain_img(self):

        # Check if in the about page contains an image

        response = self.client.get(reverse('about'))

        self.assertIn('img', response.content)



    def test_about_contains_create_message(self):

        # Check if in the about page contains the message from the exercise

        response = self.client.get(reverse('about'))

        self.assertIn('This tutorial has been put together by', response.content)





class Chapter5ViewTests(TestCase):



    def setUp(self):

        try:

            from populate_rango import populate

            populate()

        except ImportError:

            print('The module populate_rango does not exist')

        except NameError:

            print('The function populate() does not exist or is not correct')

        except:

            print('Something went wrong in the populate() function :-(')





    def get_category(self, name):



        from rango.models import Category

        try:

            cat = Category.objects.get(name=name)

        except Category.DoesNotExist:

            cat = None

        return cat



    def test_python_cat_added(self):

        cat = self.get_category('Python')

        self.assertIsNotNone(cat)



    def test_python_cat_with_views(self):

        cat = self.get_category('Python')



        self.assertEquals(cat.views, 128)



    def test_python_cat_with_likes(self):

        cat = self.get_category('Python')

        self.assertEquals(cat.likes, 64)



    def test_view_has_title(self):

        response = self.client.get(reverse('index'))



        #Check title used correctly

        self.assertIn('<title>', response.content)

        self.assertIn('</title>', response.content)



    # Need to add tests to:

    # check admin interface - is it configured and set up



    def test_admin_interface_page_view(self):

        from admin import PageAdmin

        self.assertIn('category', PageAdmin.list_display)

        self.assertIn('url', PageAdmin.list_display)





class Chapter6ViewTests(TestCase):



    def setUp(self):

        try:

            from populate_rango import populate

            populate()

        except ImportError:

            print('The module populate_rango does not exist')

        except NameError:

            print('The function populate() does not exist or is not correct')

        except:

            print('Something went wrong in the populate() function :-(')





    # are categories displayed on index page?



    # does the category model have a slug field?





    # test the slug field works..

    def test_does_slug_field_work(self):

        from rango.models import Category

        cat = Category(name='how do i create a slug in django')

        cat.save()

        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')



    # test category view does the page exist?





    # test whether you can navigate from index to a category page





    # test does index page contain top five pages?



    # test does index page contain the words "most liked" and "most viewed"



    # test does category page contain a link back to index page?





class Chapter7ViewTests(TestCase):



    def setUp(self):

        try:

            from forms import PageForm

            from forms import CategoryForm



        except ImportError:

            print('The module forms does not exist')

        except NameError:

            print('The class PageForm does not exist or is not correct')

        except:

            print('Something else went wrong :-(')



    pass


    def test_add_category_form_is_displayed_correctly(self):

        # Access add category page

        response = self.client.get(reverse('add_category'))



        # Check form in response context is instance of CategoryForm

        self.assertTrue(isinstance(response.context['form'], CategoryForm))



        # Check form is displayed correctly

        # Header

        self.assertIn('<h1>Add a Category</h1>'.lower(), response.content.lower())



        # Label

        self.assertIn('Please enter the category name.'.lower(), response.content.lower())



        # Text input

        self.assertIn('id="id_name" maxlength="128" name="name" type="text"', response.content)



        # Button

        self.assertIn('type="submit" name="submit" value="Create Category"'.lower(), response.content.lower())



    def test_add_page_form_is_displayed_correctly(self):

        # Create categories

        categories = test_utils.create_categories()



        for category in categories:

            # Access add category page

            try:

                response = self.client.get(reverse('index'))

                response = self.client.get(reverse('add_page', args=[category.slug]))

            except:

                try:

                    response = self.client.get(reverse('rango:index'))

                    response = self.client.get(reverse('rango:add_page', args=[category.slug]))

                except:

                    return False



            # Check form in response context is instance of CategoryForm

            self.assertTrue(isinstance(response.context['form'], PageForm))



            # Check form is displayed correctly



            # Label 1

            self.assertIn('Please enter the title of the page.'.lower(), response.content.lower())



            # Label 2

            self.assertIn('Please enter the URL of the page.'.lower(), response.content.lower())



            # Text input 1

            self.assertIn('id="id_title" maxlength="128" name="title" type="text"'.lower(), response.content.lower())



            # Text input 2

            self.assertIn('id="id_url" maxlength="200" name="url" type="url"'.lower(), response.content.lower())



            # Button

            self.assertIn('type="submit" name="submit" value="Add Page"'.lower(), response.content.lower())



    def test_access_category_that_does_not_exists(self):

        # Access a category that does not exist

        response = self.client.get(reverse('show_category', args=['python']))



        # Check that it has a response as status code OK is 200

        self.assertEquals(response.status_code, 200)



        # Check the rendered page is not empty, thus it was customised (I suppose)

        self.assertNotEquals(response.content, '')



    def test_link_to_add_page_only_appears_in_valid_categories(self):

        # Access a category that does not exist

        response = self.client.get(reverse('show_category', args=['python']))



        # Check that there is not a link to add page

        try:

            self.assertNotIn(reverse('add_page', args=['python']), response.content)

            # Access a category that does not exist

            response = self.client.get(reverse('show_category', args=['other-frameworks']))

            # Check that there is not a link to add page

            self.assertNotIn(reverse('add_page', args=['other-frameworks']), response.content)

        except:

            try:

                self.assertNotIn(reverse('rango:add_page', args=['python']), response.content)

                # Access a category that does not exist

                response = self.client.get(reverse('rango:show_category', args=['other-frameworks']))

                # Check that there is not a link to add page

                self.assertNotIn(reverse('rango:add_page', args=['other-frameworks']), response.content)

            except:

                return False




    def test_category_contains_link_to_add_page(self):

        # Crete categories

        categories = test_utils.create_categories()



        # For each category in the database check if contains link to add page

        for category in categories:

            try:

                response = self.client.get(reverse('show_category', args=[category.slug]))

                self.assertIn(reverse('add_page', args=[category.slug]), response.content)

            except:

                try:

                    response = self.client.get(reverse('rango:show_category', args=[category.slug]))

                    self.assertIn(reverse('rango:add_page', args=[category.slug]), response.content)

                except:

                    return False
    # test is there a PageForm in rango.forms



    # test is there a CategoryForm in rango.forms



    # test is there an add page page?



    # test is there an category page?





    # test if index contains link to add category page

    #<a href="/rango/add_category/">Add a New Category</a><br />





    # test if the add_page.html template exists
# Create your tests here.
