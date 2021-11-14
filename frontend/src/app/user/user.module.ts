import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './components/login/login.component';
import { HomeComponent } from './components/home/home.component';
import { RegisterComponent } from './components/register/register.component';
import { UserRoutingModule} from "./user.routes";
import { ReactiveFormsModule } from '@angular/forms';
import {HttpClientModule} from "@angular/common/http";


@NgModule({
  declarations: [
    LoginComponent,
    HomeComponent,
    RegisterComponent
  ],
  exports: [
    HomeComponent,
    UserRoutingModule
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule
  ]
})
export class UserModule { }