import { Component, Input, OnInit, Output } from '@angular/core';
import * as EventEmitter from 'events';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {

  // @Input() title!: string;
  // @Input() content!: string;
  // @Input() imagesource!: string;

  // @Output() myop:EventEmitter<string>= new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  // SendValue(){
  //   this.myop.emit(this.title);
  // }
}