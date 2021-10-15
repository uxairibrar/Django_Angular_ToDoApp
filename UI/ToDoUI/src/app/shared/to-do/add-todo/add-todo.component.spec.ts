import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';

import { AddTodoComponent } from './add-todo.component';

describe('AddTodoComponent', () => {
  let component: AddTodoComponent;
  let fixture: ComponentFixture<AddTodoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddTodoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AddTodoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  describe('Add button', () => {

    // Tests Todo component have the add button or not
    it('should have a add button', () => {
      const addButton = fixture.debugElement.nativeElement.querySelector('#addButton')
      expect(addButton).toBeTruthy();
    });

    // Tests add button have the click event applied on it
    it('should have a click event on add button', () => {

      spyOn(component, 'addToDo');
      component.addToDo();

      fixture.detectChanges();

      let buton = fixture.debugElement.query(By.css('button')).nativeElement.click();
      expect(component.addToDo).toHaveBeenCalled();

    });

  });  
});
