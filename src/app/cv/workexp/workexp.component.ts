import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { Injectable } from "@angular/core";
import { FormControl, FormGroup, Validators } from "@angular/forms";
import { HttpClient } from "@angular/common/http";
import { environment } from "src/environments/environment";
import { Router } from '@angular/router';
import { WorkexpService } from 'src/app/shared/workexp.service';

@Component({
  selector: 'app-workexp',
  templateUrl: './workexp.component.html',
  styleUrls: ['./workexp.component.css']
})
export class WorkexpComponent implements OnInit {

  // @Output() closeModalEvent = new EventEmitter<boolean>();
  @Output() experienceEvent = new EventEmitter<any>();
  experience: Object;
  deleteEvent: any;
  @Input() selectedExperience: any;

  constructor(
    public expService: WorkexpService,
    private router: Router) {}

  formControls = this.expService.form.controls;  
  error: string;  

  onSubmit() {    
      this.expService.form.value["username"] = localStorage.getItem("username");
      this.expService.addWorkExp(this.expService.form.value).subscribe(data => {        
        if (data["error"]) {
          this.error = data["error"];
        } 
    });   
    
  }

  sendExpInfo(){
    let  username = localStorage.getItem("username");
    this.expService.getExperience(username).subscribe(data => {
    this.experience = data;      
    this.experienceEvent.emit(data);
    });
  }

  ngOnInit() {
    this.sendExpInfo()    
    console.log("this.selectedExperience");    
  }

}
