import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";
import { LoginService } from "../shared/login.service";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.css"]
})
export class LoginComponent implements OnInit {

  constructor(
    public loginService: LoginService,
    private router: Router) {}

  formControls = this.loginService.form.controls;
  error: string;  

  onSubmit() {
    //console.log(this.loginService.form.value);
    //console.log(this.formControls.username.value);

    this.loginService.loginIn(this.loginService.form.value).subscribe(data => {
      if (data["payload"]) {
        console.log(data["payload"]);
        localStorage.setItem("isLoggedIn", "True");
        localStorage.setItem("username", this.formControls.username.value);
        // localStorage.setItem("role", data["payload"].role);
        // localStorage.setItem("email", data["payload"].email);
        this.router.navigate(["home"]);
      } else {
        this.error = data["error"];
      }
    });
  }

  register() {
    this.router.navigate(["register"]);
  }

  ngOnInit() {}
}
