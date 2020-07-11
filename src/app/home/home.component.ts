import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { HomeService } from '../shared/home.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  isLoggedIn: string;
  username: string;
  jobs : any [] = [];
  showSuccessMessage: boolean;
  noJobs: boolean;
  job: string;
  location: string;

  constructor(private router: Router, public homeService: HomeService) { }
  
  ngOnInit() {
    this.isLoggedIn = localStorage.getItem("isLoggedIn");
    this.username = localStorage.getItem("username");
    this.loadJobs()
  }

  loadJobs(){
    this.homeService.getJobs(this.username).subscribe(data =>{
      console.log(data);     
      this.jobs = data as any[];
    //   if(data == ""){
    //     // this.noJobs = true;
    //     // setTimeout(() => (this.noJobs = false), 2000);
    //   }
    //   else{
    //     this.jobs = data;
    //   }      
    });
  }

  postApplication(job_id){
    this.homeService.form.value["username"] = this.username;
    this.homeService.form.value["job_id"] = job_id;  
    
    this.homeService.postJob(this.homeService.form.value).subscribe(arg => {
      console.log(arg);
      
      if(arg["success"] == "success"){
        this.showSuccessMessage = true;
        setTimeout(() => (this.showSuccessMessage = false), 2000);
      }        
    });
        
  }

  signOut(){
    localStorage.clear();
    this.router.navigate(["home"]);
  }

}
