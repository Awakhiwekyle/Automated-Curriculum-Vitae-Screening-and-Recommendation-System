import { EducationService } from './../../shared/education.service';
import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-education',
  templateUrl: './education.component.html',
  styleUrls: ['./education.component.css']
})
export class EducationComponent implements OnInit {

  @Output() educationEvent = new EventEmitter<any>();
  education: Object;

  constructor(public eduService: EducationService) {}

  error: string;  

  onSubmit() {    
      this.eduService.form.value["username"] = localStorage.getItem("username");
      this.eduService.educationalData(this.eduService.form.value).subscribe(data => {        
        if (data["error"]) {
          this.error = data["error"];
        } 
    });   
    
  }

  sendEduInfo(){
    let  username = localStorage.getItem("username");
    this.eduService.getEducation(username).subscribe(data => {
    this.education = data;      
    this.educationEvent.emit(data);
    });
  }

  updateEducation(value: any) {
    throw new Error("Method not implemented.");
  }

  ngOnInit() {
    this.sendEduInfo()
  }

}
