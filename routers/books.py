from fastapi import APIRouter, HTTPException, status
from typing import Annotated
from repository import BookRepository
from schemas.books import SBook, SBookAdd
from database import SessionDep

router = APIRouter(prefix="/books", tags=["Книги"])

@router.post("", status_code=status.HTTP_201_CREATED, response_model=SBook)
async def create_book(book: SBookAdd, session: SessionDep):
    result_book = await BookRepository.add_book(book, session)
    return result_book

@router.get("", status_code=status.HTTP_200_OK, response_model=list[SBook])
async def get_all_book(session: SessionDep):
    result_get_books = await BookRepository.find_books(session)
    return result_get_books

@router.get("/{id}", response_model=SBook)
async def get_one_book(id: int, session: SessionDep):
    result_get_book = await BookRepository.find_one_book(id,session)
    if result_get_book:
        return result_get_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Книга не найдена")
        
@router.put("/{id}", response_model=SBook)
async def updated_books(id: int, book: SBookAdd, session: SessionDep):
    result_update_book = await BookRepository.update_book(id, book, session)
    if result_update_book:
        return result_update_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def deleted_books(id: int, session: SessionDep):
    result_delete_book = await BookRepository.delete_book(id, session)
    if result_delete_book:
        return None
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
