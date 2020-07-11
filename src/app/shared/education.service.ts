import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { environment } from 'src/environments/environment';
import { map } from "rxjs/operators";
import { keepFresh } from "http-operators";

@Injectable({
  providedIn: 'root'
})
export class EducationService {

  constructor(private http_: HttpClient) {}

  form = new FormGroup({
    degree: new FormControl("", Validators.required),
    school: new FormControl("", Validators.required),
    city: new FormControl("", Validators.required),
    fieldOfStudy: new FormControl("", Validators.required),
    duration: new FormControl("", Validators.required),
    username: new FormControl("", Validators.required),
  },
  );

  url = environment.baseUrl;

  educationalData(edu) {
    // console.log(person);    
    return this.http_.post(`${this.url}/newEducation`, edu);
  }

  getEducation(username) {    
    return this.http_.get(`${this.url}/getEducation/${username}`).pipe(
      map(result => result),
      // keepFresh(2000)
    ).pipe();
  }
}
