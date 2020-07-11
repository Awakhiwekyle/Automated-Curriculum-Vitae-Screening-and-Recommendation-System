import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { environment } from 'src/environments/environment';
import { map } from "rxjs/operators";
import { keepFresh } from "http-operators";

@Injectable({
  providedIn: 'root'
})
export class SKillService {

  constructor(private http_: HttpClient) {}

  form = new FormGroup({
    skill: new FormControl("", Validators.required),
    experience: new FormControl("", Validators.required),    
    username: new FormControl("", Validators.required),
  },
  );

  url = environment.baseUrl;

  skillData(skill) {
    // console.log(person);    
    return this.http_.post(`${this.url}/newSkill`, skill);
  }

  getSkills(username) {    
    return this.http_.get(`${this.url}/getSkills/${username}`).pipe(
      map(result => result),
      // keepFresh(2000)
    ).pipe();
  }

  updateSkills(id){
    return this.http_.patch(`${this.url}/updateSkill`, id);
  }
}
