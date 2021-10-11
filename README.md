# booksapi
Django rest api app for book database




###  These are the different api endpoints provided by app  ###


1.GET     /api/external-books/?name=book_name
   JSON response with book details from iceandfire api
  Ex : /api/external-books/?name=A Game of Thrones

 
 
 
 
 
 
 
2. POST       /api/v1/books
   Create a book in database with provided details
    All of following values need to be specified --
     name
     isbn
     authors
     country
     number_of_pages
     publisher
     release_date
     
     
     
     
     
     
     
     
3.  GET     /api/v1/books'
    Return information of all the books in database
  
    query parameters --- name,country,publisher,release_date
    /api/v1/books/?name=book_name
    returns json response with  details of book with matching parameter
   
   Example Responese:
   
               {
             "status_code": 200,
             "status": "success",
             "data": {
             "id": 1,
             "name": "My First Book",
             "isbn": "123-3213243567",
             "authors": [
             "John Doe"
             ],
             "number_of_pages": 350,
             "publisher": "Acme Books Publishing",
             "country": "United States",
             "release_date": "2019-01-01"
             }
            }
   
 
 
 
 
 
 
 
4. POST        /api/v1/books/:id/delete
  to delete a book with provided id
  
  
  
  
  
 
 5. POST        /api/v1/books/:id/update
 
  to update a book infomation with specific id
  can be accessed with any of following data values
     name
     isbn
     authors
     country
     number_of_pages
     publisher
     release_date
  
  
  
  
  
 
 6. GET        /api/v1/books/:id
 
  to get a book information  with specific id
 
 
