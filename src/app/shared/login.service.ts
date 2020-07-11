import { Injectable } from "@angular/core";
import { FormControl, FormGroup, Validators } from "@angular/forms";
import { HttpClient } from "@angular/common/http";
import { environment } from "src/environments/environment";

@Injectable({
  providedIn: "root"
})
export class LoginService {
  constructor(private http_: HttpClient) {}

  form = new FormGroup({
    username: new FormControl("", Validators.required),
    password: new FormControl("", Validators.required)
  });

  url = environment.baseUrl;
  //login
  loginIn(user) {
    console.log(`${this.url}/login`);

    return this.http_.post(`${this.url}/login`, user);
  }
}
