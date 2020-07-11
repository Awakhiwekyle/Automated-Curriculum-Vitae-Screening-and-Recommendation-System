import { SKillService } from './../../shared/skill.service';
import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-skill',
  templateUrl: './skill.component.html',
  styleUrls: ['./skill.component.css']
})
export class SkillComponent implements OnInit {
  @Output() skillsEvent = new EventEmitter<any>();
  skills: {};
  error: any;

  constructor(public skillService: SKillService) { }

  onSubmit() {
    // Object.keys(this.skill).length !== 0
    if(false){          
      //this.updateSkill(this.skillService.form.value);
    }
    else{
      console.log("Submit skill");
      
      this.skillService.form.value["username"] = localStorage.getItem("username");
      this.skillService.skillData(this.skillService.form.value).subscribe(data => {
        if (data["error"]) {
          this.error = data["error"];
        } 
    });
    }
    
  }

  sendSkillsInfo(){
    let  username = localStorage.getItem("username");
    this.skillService.getSkills(username).subscribe(data => {
    this.skills = data;
    this.skillsEvent.emit(data);
    });
  }

  // editPersonalData(){
  //   let username = localStorage.getItem("username");
  //   this.skillService.getSkills(username).subscribe(data => {      
  //     let  x = {};
  //     x["name"] = data["name"];
  //     x["surname"] = data["surname"];
  //     x["mobile"] = data["mobile"];
  //     x["email"] = data["email"];
  //     x["city"] = data["city"];
  //     x["country"] = data["country"];
  //     x["username"] = data["username"];      
  //     this.skillService.form.setValue(x);
  //     this.person = x;
  // });
  // }

  updateSkill(skill){
    this.skillService.updateSkills(skill).subscribe(data => {
      if (data["error"]) {
        this.error = data["error"];
      }     
    });
  }



  ngOnInit() {
    this.sendSkillsInfo();
    // this.editPersonalData();
  }

}

