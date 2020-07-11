import { Component, OnInit, Output, EventEmitter, Input } from '@angular/core';
import { Router } from '@angular/router';
import { PersonalService } from '../shared/personal.service';
import { WorkexpService } from '../shared/workexp.service';

@Component({
  selector: 'app-cv',
  templateUrl: './cv.component.html',
  styleUrls: ['./cv.component.css']
})
export class CvComponent implements OnInit {
  isLoggedIn: string;
  username: string;
  modalVisible = false;
  isVisible = false;
  name: string;
  surname: any;
  mobile: any;
  country: any;
  city: any;
  email: string;
  jobtitle: any;
  company: any;
  years: any;
  months: any;
  description: any;
  experiences = [];
  education: any;
  error: any;
  selectedExperience: any;
  skills: any;
  uploadVisible: boolean;

  constructor(private router: Router, public personalService: PersonalService, public expService: WorkexpService, ) { }  
  
  ngOnInit() {
    this.isLoggedIn = localStorage.getItem("isLoggedIn");
    this.username = localStorage.getItem("username");    
  }

  signOut(){
    localStorage.clear();
    this.router.navigate(["home"]);
  }

  receivePersonal($event){
    this.name = $event["name"];
    this.surname = $event["surname"];
    this.mobile = $event["mobile"];
    this.country = $event["country"]; 
    this.city = $event["city"];
    this.email = $event["email"];
  }

  receiveExperience($event){  
    this.experiences = $event;       
  }

  receiveSkills($event){  
    this.skills = $event;       
  }

  receiveEducation($event){  
    this.education = $event; 
  }

  updateExperience(experience){  
    console.log(experience);      
    this.selectedExperience = experience;
  }

  delete(id){
    this.expService.deleteExperience(id).subscribe(data =>{
      console.log(data);
    });
  }

  showUpload(){
    this.uploadVisible = !this.uploadVisible;
  }

}
