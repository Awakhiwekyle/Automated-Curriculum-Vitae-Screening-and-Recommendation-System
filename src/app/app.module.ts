import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { MenuComponent } from './menu/menu.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { EmployeesComponent } from './employees/employees.component';
import { HomeComponent } from './home/home.component';
import { CvComponent } from './cv/cv.component';
import { WorkexpComponent } from './cv/workexp/workexp.component';
import { PersonalComponent } from './cv/personal/personal.component';
import { map } from "rxjs/operators";
import { keepFresh } from "http-operators";
import { EducationComponent } from './cv/education/education.component';
import { SkillComponent } from './cv/skill/skill.component';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    MenuComponent,
    DashboardComponent,
    EmployeesComponent,
    HomeComponent,
    CvComponent,
    WorkexpComponent,
    PersonalComponent,
    EducationComponent,
    SkillComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    Ng2SearchPipeModule,
    FormsModule
  ],
  providers: [HttpClientModule],
  bootstrap: [AppComponent]
})
export class AppModule { }
