import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'table';
  words:{Books:string,Author:string,Price:any}[]=[
    {Books:"The words",Author:"John",Price:1233},
    {Books:"The price",Author:"Selva",Price:3124},
    {Books:"The Author",Author:"Devil",Price:4324},
    {Books:"The book",Author:"Sam",Price:5467}
  ]

}
