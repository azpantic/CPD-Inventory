from .db import db
from .models import Item, User, Operation

class FDataBase():
    
    def getUserById(self , user_id : str) -> User:
        
        user = db.session.query(User).get(user_id)
        
        return user
    
    def getUserByEmail(self , email : str) -> User:
        
        users = db.session.query(User).where(User.email == email)
        
        if users.count() == 0:
            return None
        
        return list(users)[0]
    
    # One page have 20 items
    def getItemsByPage(self, pageNumber : int) -> list[Item]:
        
        items = db.session.query(Item).all()
        
        return list(items)
    
    def getItemById(self, id : int) -> Item:
        
        item = db.session.query(Item).get(id)
        
        return item
    
    def addItem(self, newItem : Item) -> None:
        
        db.session.add(newItem)
        db.session.commit()
    
    def addUser(self, newUser : User) -> None:
            
        db.session.add(newUser)
        db.session.commit()
        
    def changeItem(self, id : int, newItem : Item) -> None:
        
        item : Item = db.session.query(Item).get(id)
         
        item.title = newItem.title
        item.cellId = newItem.cellId
        item.count = newItem.count
        item.description = item.description
        
        db.session.commit()
        
    def takeItem(self, id : int , amount : int) -> None:
        item : Item = db.session.query(Item).get(id)
        
        item.count -= amount
        
        db.session.commit()
        
    def registerNewOperation(self, newOperation : Operation) -> None:
        db.session.add(newOperation)
        
        db.session.commit()
        
    def getUserOperations(self, user_id) -> list[Operation]:
        
        return list(db.session.query(Operation).where(Operation.user_id == user_id))
        
    def searchForItems(self,  search : str) -> list[Item]:
        
        return list(db.session.query(Item).filter(Item.title.like(f"%{search}%")))    
    
dBase : FDataBase = FDataBase()