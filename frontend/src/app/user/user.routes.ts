import { NgModule } from '@angular/core';
import { Routes, RouterModule } from "@angular/router";
import { HomeComponent} from "./components/home/home.component";
import {LoginComponent} from "./components/login/login.component";

const USER_ROUTES: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'login', component: LoginComponent},
  {path: '**', pathMatch: 'full', redirectTo: 'home'}
];

@NgModule({
  imports: [RouterModule.forRoot(USER_ROUTES)],
  exports: [RouterModule]
})
export class UserRoutingModule {}
