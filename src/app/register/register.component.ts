import { Component, OnInit } from '@angular/core';
import { RegisterService } from '../shared/register.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(
    public registerService: RegisterService,
    private router: Router
  ) {}

  formControls = this.registerService.form.controls;
  error: string;

  onSubmit() {
    //console.log(this.registerService.form.value);
    this.registerService
      .registerUser(this.registerService.form.value)
      .subscribe(data => {
        console.log(data);
        if (data["error"]) {
          this.error = data["error"];
        }
        else if(this.formControls["password"] !== this.formControls["confirmPassword"]){
          this.error = "Passwords do not match";
        }
        else {
          localStorage.setItem("isLoggedIn", "True");
          localStorage.setItem("username", this.formControls.username.value);
          this.router.navigate(["home"]);
        }
      });
  }

  

  login() {
    this.router.navigate(["login"]);
  }

  ngOnInit() {
  }

}
