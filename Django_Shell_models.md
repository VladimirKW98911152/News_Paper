(venv) PS C:\Konspecti_i_Uchoba\News_Paper\project> python manage.py shell
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from news.models import *
>>> u1 = User.objects.create_user(username='Petya')
>>> u1
<User: Petya>
>>> u2 = User.objects.create_user(username='Vasya')
>>> u2
<User: Vasya>
>>> Author.objects.create(authorUser=u1)
<Author: Author object (1)>
>>> Author.objects.create(authorUser=u2)
<Author: Author object (2)>
>>> Category.objects.create(name='Sociologiya')
<Category: Category object (1)>
>>> Category.objects.create(name='Pravo')
<Category: Category object (2)>
>>> Category.objects.create(name='Nauka')
<Category: Category object (3)>
>>> Category.objects.create(name='Tehnika')
<Category: Category object (4)>
>>> author = Author.objects.get(id=1)
>>> author
<Author: Author object (1)>
>>> Post.objects.create(author=author, categoryType='NW', title='Как проводить исследование', text='Чем больше выборка при проведении социологических ис
следований, тем выше репрезентативность этих исследований и тем точнее результаты исследования отражают социальные процессы, происходящие в обществе')
<Post: Post object (1)>
>>> author = Author.objects.get(id=2)
>>> author
<Author: Author object (2)>
>>> Post.objects.create(author=author, categoryType='NW', title='Подорожание автомобилей', text='В настоящее время наблюдаются очень высокие темпы подор
ожания автотранспортной техники в связи с изменением курса валют, влекущего увеличение стоимости комплектующих, поставляемых из-за рубежа')
<Post: Post object (2)>
>>> author = Author.objects.get(id=1)
>>> author
<Author: Author object (1)>
>>> author
<Author: Author object (1)>
>>> Post.objects.create(author=author, categoryType='AR', title='Изменения в законодательстве', text='В 2013 году, в Уголовно-Процессуальный кодекс РФ б
ыли внесены изменения, так статья 170 была дополнена случаями, когда следователь может привлекать понятых к участию в некоторых следственных действиях п
о своему усмотрению, но в случае, если понятые не принимали участия в следственном действии, то необходимо применение технических средств фиксации хода
и результатов следственого действия')
<Post: Post object (3)>
>>> author = Author.objects.get(id=2)
>>> author
<Author: Author object (2)>
>>> Post.objects.create(author=author, categoryType='AR', title='Принцип Питера', text='Принцип Питера, одно из негативных явлений в менеджменте любой о
рганизации, согласно данному принципу, если человек, при перемещении на вышестоящие должности достигает порога своей компетенции, он не может эффективно
 работать на занимаемой должности, и пользуясь своим положением, начинает придумывать ненужные лишние системы отчетности, увеличивая бюрократию, снижая
эввективность работы всей организации')
<Post: Post object (4)>
>>> Post.objects.get(id=3).text
'В 2013 году, в Уголовно-Процессуальный кодекс РФ были внесены изменения, так статья 170 была дополнена случаями, когда следователь может привлекать пон
ятых к участию в некоторых следственных действиях по своему усмотрению, но в случае, если понятые не принимали участия в следственном действии, то необх
одимо применение технических средств фиксации хода и результатов следственого действия'
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
>>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
>>> Post.objects.get(id=4).postCategory.add(Category.objects.get(id=4))
>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='Вот это да, мы этого и не знали')
<Comment: Comment object (1)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Я и пешком по хожу))')
<Comment: Comment object (2)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=1).authorUser, text='Да здравствует фотошоп')
<Comment: Comment object (3)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=Author.objects.get(id=2).authorUser, text='И где же он интересно себя проявля
ет')
<Comment: Comment object (4)>
>>> Comment.objects.get(id=1).deslike()
>>> Comment.objects.get(id=1).deslike()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=2).deslike()
>>> Comment.objects.get(id=2).deslike()
>>> Comment.objects.get(id=2).deslike()
>>> Comment.objects.get(id=2).deslike()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=3).deslike()
>>> Comment.objects.get(id=3).deslike()
>>> Comment.objects.get(id=3).deslike()
>>> Comment.objects.get(id=3).deslike()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).deslike()
>>> Comment.objects.get(id=4).deslike()
>>> Comment.objects.get(id=4).deslike()
>>> Comment.objects.get(id=1).rating
2
>>> Comment.objects.get(id=2).rating
3
>>> Comment.objects.get(id=3).rating
2
>>> Comment.objects.get(id=4).rating
3
>>> Post.objects.get(id=1).dislike()
>>> Post.objects.get(id=1).dislike()
>>> Post.objects.get(id=1).dislike()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=2).like()
>>> Post.objects.get(id=2).like()
>>> Post.objects.get(id=2).like()
>>> Post.objects.get(id=2).like()
>>> Post.objects.get(id=2).like()
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=3).dislike()
>>> Post.objects.get(id=3).dislike()
>>> Post.objects.get(id=3).dislike()
>>> Post.objects.get(id=3).like()
>>> Post.objects.get(id=3).like()
>>> Post.objects.get(id=3).like()
>>> Post.objects.get(id=3).like()
>>> Post.objects.get(id=3).like()
>>> Post.objects.get(id=4).like()
>>> Post.objects.get(id=4).like()
>>> Post.objects.get(id=4).like()
>>> Post.objects.get(id=4).like()
>>> Post.objects.get(id=4).like()
>>> Post.objects.get(id=4).dislike()
>>> Post.objects.get(id=4).dislike()
>>> Post.objects.get(id=4).dislike()
>>> Post.objects.get(id=1).rating
-11
>>> Post.objects.get(id=2).rating
-7
>>> Post.objects.get(id=3).rating
-8
>>> Post.objects.get(id=4).rating
-8
>>> Author.objects.get(id=1)
<Author: Author object (1)>
>>> a=Author.objects.get(id=1)
>>> a.update_rating()
>>> a=Author.objects.get(id=1)
>>> a.update_rating()
>>> a.ratingAuthor
-53
>>> Author.objects.get(id=2)
<Author: Author object (2)>
>>> a=Author.objects.get(id=1)
>>> a.update_rating()
>>> a.ratingAuthor
-53
>>> a=Author.objects.get(id=2)
>>> a.update_rating()
>>> a.ratingAuthor
-39
>>> a=Author.objects.order_by('-ratingAuthor')[:1]
>>> a
<QuerySet [<Author: Author object (2)>]>
>>> a=Author.objects.order_by('-ratingAuthor')[:2]
>>> a
<QuerySet [<Author: Author object (2)>, <Author: Author object (1)>]>
>>> a=Author.objects.order_by('-ratingAuthor')
>>> a
<QuerySet [<Author: Author object (2)>, <Author: Author object (1)>]>
>>> for i in a:
...     i.ratingAuthor
...     i.authorUser.username
...
-39
'Vasya'
-53
'Petya'
>>>
>>> exit()
(venv) PS C:\Konspecti_i_Uchoba\News_Paper\project>
