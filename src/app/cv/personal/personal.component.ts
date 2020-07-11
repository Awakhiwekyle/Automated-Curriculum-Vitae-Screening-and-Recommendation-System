import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { PersonalService } from 'src/app/shared/personal.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-personal',
  templateUrl: './personal.component.html',
  styleUrls: ['./personal.component.css']
})
export class PersonalComponent implements OnInit {
  @Output() personalEvent = new EventEmitter<any>();
  person = null;

  constructor(
    public personalService: PersonalService,
    private router: Router) {}

  formControls = this.personalService.form.controls;
  error: string;  

  onSubmit() {
    if(Object.keys(this.person).length !== 0){          
      this.updatePerson(this.personalService.form.value);
    }
    else{
      this.personalService.form.value["username"] = localStorage.getItem("username");
      this.personalService.personalData(this.personalService.form.value).subscribe(data => {
        if (data["error"]) {
          this.error = data["error"];
        } 
    });
    }
    
  }

  sendPersonalInfo(){
    let  username = localStorage.getItem("username");
    this.personalService.getPerson(username).subscribe(data => {
    this.person = data;
    this.personalEvent.emit(data);
    });
  }

  editPersonalData(){
    let username = localStorage.getItem("username");
    this.personalService.getPerson(username).subscribe(data => {      
      let  x = {};
      x["name"] = data["name"];
      x["surname"] = data["surname"];
      x["mobile"] = data["mobile"];
      x["email"] = data["email"];
      x["city"] = data["city"];
      x["country"] = data["country"];
      x["username"] = data["username"];      
      this.personalService.form.setValue(x);
      this.person = x;
  });
  }

  updatePerson(person){
    this.personalService.updatePerson(person).subscribe(data => {
      if (data["error"]) {
        this.error = data["error"];
      }     
    });
  }



  ngOnInit() {
    this.sendPersonalInfo();
    this.editPersonalData();
  }

}
