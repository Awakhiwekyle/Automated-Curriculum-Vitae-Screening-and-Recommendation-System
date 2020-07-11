import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { environment } from 'src/environments/environment';
import { map } from "rxjs/operators";
import { keepFresh } from "http-operators";

@Injectable({
  providedIn: 'root'
})
export class HomeService {
  
  constructor(private http_: HttpClient) {}

  form = new FormGroup({
    job_id: new FormControl("", Validators.required),    
    username: new FormControl("", Validators.required),
  },
  );

  url = environment.baseUrl;

  postJob(application) {
    console.log(application);    
    return this.http_.post(`${this.url}/postApplication`, application);
  }

  getJobs(username) {    
    return this.http_.get(`${this.url}/getJobs/${username}`).pipe(
      map(result => result),
      // keepFresh(2000)
    );
  }

  updateSkills(id){
    return this.http_.patch(`${this.url}/updateSkill`, id);
  }

  
}
