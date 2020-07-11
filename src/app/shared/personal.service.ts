import { Injectable } from "@angular/core";
import { FormControl, FormGroup, Validators } from "@angular/forms";
import { HttpClient } from "@angular/common/http";
import { environment } from "src/environments/environment";
import { map } from "rxjs/operators";
import { keepFresh } from "http-operators";

@Injectable({
  providedIn: 'root'
})
export class PersonalService {

  constructor(private http_: HttpClient) {}

  form = new FormGroup({
    name: new FormControl("", Validators.required),
    surname: new FormControl("", Validators.required),
    mobile: new FormControl("", Validators.required),
    email: new FormControl("", Validators.required),
    city: new FormControl("", Validators.required),
    country: new FormControl("", Validators.required),    
    username: new FormControl("", Validators.required),    
  },
  );

  url = environment.baseUrl;

  //Register
  personalData(person) {
    // console.log(person);    
    return this.http_.post(`${this.url}/newPerson`, person);
  }

  getPerson(username) {    
    return this.http_.get(`${this.url}/getPerson/${username}`);
  }
  
  updatePerson(person){
    return this.http_.patch(`${this.url}/updatePerson`, person);
  }

}
