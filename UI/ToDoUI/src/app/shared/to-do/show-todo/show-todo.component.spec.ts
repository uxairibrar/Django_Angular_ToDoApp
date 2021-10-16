import { NO_ERRORS_SCHEMA } from '@angular/core';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { ToDoComponent } from '../to-do.component';

import { ShowTodoComponent } from './show-todo.component';

describe('ShowTodoComponent', () => {
  let component: ShowTodoComponent;
  let fixture: ComponentFixture<ShowTodoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowTodoComponent ],
      schemas: [NO_ERRORS_SCHEMA]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowTodoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  
  // Smoke Test
  // Test the presence of a Component instance
  it('should be created', () => {
    expect(component).toBeTruthy();
  });

  // Tests whether show-todo compnent is rendering the todo component or not
  it('renders a show to do component', () => {
    const { debugElement } = fixture;
    const counter = debugElement.query(By.css('app-add-todo'));
    expect(counter).toBeTruthy();
  });

  // Tests whether show-todo compnent have the table element or not
  it('should have a table', () => {
    const table = fixture.debugElement.nativeElement.querySelector('#tableID')
    expect(table).toBeTruthy();
  });


  describe('Add button', () => {

    // Tests Todo component have the add button or not
    it('should have a add button', () => {
      const addButton = fixture.debugElement.nativeElement.querySelector('#addButton')
      expect(addButton).toBeTruthy();
    });


    // Tests add button have the click event applied on it
    it('should have a click event on add button', () => {

      spyOn(component, 'addClick');
      component.addClick();

      fixture.detectChanges();

      let buton = fixture.debugElement.query(By.css('button')).nativeElement.click();
      expect(component.addClick).toHaveBeenCalled();

    });

  });  

  describe('Close button', () => {

    // Tests Todo component have the close button or not
    it('should have a close button', () => {
      const closeButton = fixture.debugElement.nativeElement.querySelector('#closeButton')
      expect(closeButton).toBeTruthy();
    });


    // Tests close button have the click event applied on it
    it('should have a click event on close button', () => {

      spyOn(component, 'closeClick');
      component.closeClick();

      fixture.detectChanges();

      let buton = fixture.debugElement.query(By.css('button')).nativeElement.click();
      expect(component.closeClick).toHaveBeenCalled();

    });

  });  

});
