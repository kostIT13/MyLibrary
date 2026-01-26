from sqlalchemy.ext.asyncio import AsyncSession
from models.books import BooksModel
from schemas.books import SBookAdd
from sqlalchemy import select, update, delete

class BookRepository:
    @classmethod
    async def add_book(cls, data: SBookAdd, session: AsyncSession) -> BooksModel:
        book_dict = data.model_dump()
        book = BooksModel(**book_dict)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book
    
    @classmethod
    async def find_books(cls, session: AsyncSession):
        query = select(BooksModel)
        result = await session.execute(query)
        books_model = result.scalars().all()
        return books_model
    
    @classmethod
    async def find_one_book(cls, book_id:int, session: AsyncSession):
        query = select(BooksModel).where(BooksModel.id == book_id)
        result = await session.execute(query)
        book_model = result.scalar_one_or_none()
        return book_model
    
    @classmethod
    async def update_book(cls, book_id:int, book: SBookAdd, session: AsyncSession):
        update_book = book.model_dump()
        query = update(BooksModel).where(BooksModel.id == book_id).values(**update_book).returning(BooksModel)
        result = await session.execute(query)
        new_book_model = result.scalar_one_or_none()
        await session.commit()
        return new_book_model
    
    @classmethod
    async def delete_book(cls, book_id: int, session: AsyncSession):
        query = select(BooksModel).where(BooksModel.id == book_id)
        result = await session.execute(query)
        exists = result.scalar_one_or_none() is not None 
        if not exists:
            return False
        
        delete_query = delete(BooksModel).where(BooksModel.id == book_id)
        await session.execute(delete_query)
        await session.commit()
        return True

