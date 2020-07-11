import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { LoginComponent } from "./login/login.component";
import { RegisterComponent } from './register/register.component';
import { MenuComponent } from './menu/menu.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { EmployeesComponent } from './employees/employees.component';
import { HomeComponent } from './home/home.component';
import { CvComponent } from './cv/cv.component';


const routes: Routes = [
  { path: "login", component: LoginComponent },
  { path: "register", component: RegisterComponent },
  { path: "home", component: HomeComponent },
  { path: "cv", component: CvComponent },

  { path: "", redirectTo: "/login", pathMatch: "full" },
  {
    path: "menu",
    component: MenuComponent,
    children: [
      { path: "dashboard", component: DashboardComponent },
      { path: "employees", component: EmployeesComponent },
    ],
    runGuardsAndResolvers: "always"
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { onSameUrlNavigation: "reload" })],
  exports: [RouterModule]
})
export class AppRoutingModule {}
export const routingComponents = [LoginComponent];
