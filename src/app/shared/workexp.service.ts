import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { environment } from 'src/environments/environment';
import { map } from "rxjs/operators";
import { keepFresh } from "http-operators";

@Injectable({
  providedIn: 'root'
})
export class WorkexpService {

  constructor(private http_: HttpClient) {}

  form = new FormGroup({
    jobtitle: new FormControl("", Validators.required),
    company: new FormControl("", Validators.required),
    city: new FormControl("", Validators.required),
    currently: new FormControl("", Validators.required),
    years: new FormControl("", Validators.required),
    months: new FormControl("", Validators.required),
    description: new FormControl("", Validators.required),
    username: new FormControl("", Validators.required),
  },
  );

  url = environment.baseUrl;  

  addWorkExp(experience) {
    console.log(experience);    
    return this.http_.post(`${this.url}/newExperience`, experience)
  }

  getExperience(username) {    
    return this.http_.get(`${this.url}/getExperience/${username}`).pipe(
      map(result => result),
      // keepFresh(2000)
    ).pipe();
  }

  deleteExperience(id) {       
    return this.http_.get(`${this.url}/deleteExperience/${id}`)
  }
  
  updateExperience(experience){
    return this.http_.patch(`${this.url}/updateExperience`, experience);
  }

}
