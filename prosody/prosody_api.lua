
-- A test file to tweak my skills with the server

CFG_SOURCEDIR='/usr/lib/prosody';
CFG_CONFIGDIR='/etc/prosody';
CFG_PLUGINDIR='/usr/lib/prosody/modules/';
CFG_DATADIR='/var/lib/prosody';

-- -- -- -- -- -- -- ---- -- -- -- -- -- -- -- --

if CFG_SOURCEDIR then
        package.path = CFG_SOURCEDIR.."/?.lua;"..package.path
        package.cpath = CFG_SOURCEDIR.."/?.so;"..package.cpath
end

if CFG_DATADIR then
        if os.getenv("HOME") then
                CFG_DATADIR = CFG_DATADIR:gsub("^~", os.getenv("HOME"));
        end
end


-- Required to be able to find packages installed with luarocks
pcall(require, "luarocks.require")

config = require "core.configmanager"
local umanager = require "core.usermanager"

local data_path = config.get("*", "core", "data_path") or CFG_DATADIR or "data";
require "util.datamanager".set_data_path(data_path);

-- What all functions do we want in the API ? Here's a tentitive list of a few of them
-- 1. createUser(username, password, host)
-- 2. deleteUser(username, host)
-- 3. addBuddy -- To be sorted out! 

function createUser(username, password, host)

		umanager.create_user(username, password, host)
		
end

function deleteUser(username, host)
		-- 
		umanager.create_user(username, nil, host)
end		

function isUser(username, host)
		
		return umanager.user_exists(username, host)
		
end
